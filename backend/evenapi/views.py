from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.http import HttpResponse

def evenapipost(response):
    b = {
          "productTypes": [
            "loan",
            "other"
          ],
          "personalInformation": {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john@example.com",
            "city": "New York",
            "state": "NY",
            "primaryPhone": "2125556789",
            "address1": "45 West 21st Street",
            "address2": "5th Floor",
            "zipcode": "10010",
            "dateOfBirth": "1993-10-09",
            "ssn": "111-22-3333"
          },
          "loanInformation": {
            "purpose": "home_refi",
            "loanAmount": 10000
          },
          "mortgageInformation": {
            "propertyStatus": "own_with_mortgage"
          },
          "creditInformation": {
            "providedCreditRating": "excellent",
            "providedNumericCreditScore": 750
          },
          "financialInformation": {
            "employmentStatus": "employed",
            "employmentPayFrequency": "weekly",
            "annualIncome": 120000
          },
          "educationInformation": {
            "educationLevel": "masters",
            "graduateDegreeType": "master_of_science",
            "universityAttended": "Johns Hopkins University"
          },
          "coApplicantInformation": {
            "firstName": "Jane",
            "lastName": "Doe",
            "dateOfBirth": "1984-03-06",
            "annualIncome": 100000,
            "streetAddress1": "45 West 21st Street",
            "streetAddress2": "5th Floor",
            "city": "New York",
            "state": "NY",
            "zipcode": "10010"
          },
          "legalInformation": {
            "consentsToFcra": True,
            "consentsToTcpa": True,
            "tcpaLanguage": "I agree to be contacted by Even Financial and its partners at the telephone number(s) I have provided above to explore personal loan offers, including contact through automatic dialing systems, artificial or pre-recorded voice messaging, or text message. I understand my consent is not required as a condition to purchasing any goods or services from anyone."
          },
          "clientTags": {
            "hello": [
              "world",
              "there"
            ],
            "something": [
              "else"
            ]
          }
        }
    a = json.dumps(b)
    return HttpResponse(a, content_type='application/json')

def evenapiget(response):
    a = {
          "uuid": "2c6cb6e4-0aa2-4ab5-9109-8679de537e10",
          "leadUuid": "f823a7c0-586a-4fc3-9cfa-c38694b80b2c",
          "loanOffers": [
            {
              "uuid": "fef16e91-960f-4ac7-a8ec-98d7a6b32c7e",
              "originator": "<Originator>",
              "originatorId": None,
              "termLength": 36,
              "termUnit": "month",
              "maxAmount": 25000,
              "minAmount": 1500,
              "maxApr": 35.99,
              "minApr": 25.01,
              "meanApr": 30.5,
              "feeRate": None,
              "maxFeeRate": None,
              "minFeeRate": None,
              "feeFixed": None,
              "maxFeeFixed": None,
              "minFeeFixed": None,
              "allowPrepayment": True,
              "prepaymentFee": 0,
              "monthlyPayment": 119.3,
              "maxMonthlyPayment": 137.4,
              "minMonthlyPayment": 119.3,
              "meanMonthlyPayment": 128.18,
              "maxTotalPayment": 4947,
              "minTotalPayment": 4295,
              "meanTotalPayment": 4615,
              "terms": None,
              "url": "https://offers.evenfinancial.com/ref/fef16e91-960f-4ac7-a8ec-98d7a6b32c7e",
              "preQualified": False,
              "preApproved": False,
              "sponsored": False,
              "aprType": "fixed",
              "recommendationScore": 95
            }
          ],
          "specialOffers": [
            {
              "uuid": "6a43bd3d-67ba-4cdf-9fb0-c137b869fb26",
              "name": "Resolve Your Debt",
              "desc": "Apply today for our customized debt resolution solutions and join thousands of other customers on the road to financial freedom.",
              "url": "https://offers.evenfinancial.com/ref/6cecafe3-78fb-40b5-9775-41dbb0537ca0",
              "partnerName": "Freedom Debt Relief",
              "partnerImageUrl": "https://aff-tag.evenfinancial.com/images/freedom/debt-relief/fdr.png",
              "recommendationScore": 76
            }
          ],
          "savingsOffers": [],
          "creditCardOffers": [],
          "mortgageOffers": [],
          "pendingResponses": [
            {
              "partner": {
                "uuid": "91d08be0-2a8c-4d28-b399-7e1b38e2522e",
                "name": "Lending Club",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "disclaimer": "Cras vestibulum diam sed tempor sagittis.",
                "imageUrl": "https://images.evenfinancial.com/old/images/lendingclub/lendingclub_120.png"
              },
              "productTypes": [
                "loan"
              ]
            }
          ],
          "pendingOriginators": [
            {
              "key": "avant",
              "name": "Avant",
              "description": "Personal loans from $1,000 to $35,000",
              "images": [
                {
                  "sizeKey": "150",
                  "url": "aff-tag.evenfinancial.com/images/avant/avant_120.png"
                },
                {
                  "sizeKey": "115",
                  "url": "aff-tag.evenfinancial.com/images/avant/avant_120.png"
                }
              ],
              "disclaimer": "Suspendisse rhoncus magna erat, nec rhoncus leo elementum eget."
            }
          ]
        }
    b = json.dumps(a)
    return HttpResponse(b, content_type='application/json')
