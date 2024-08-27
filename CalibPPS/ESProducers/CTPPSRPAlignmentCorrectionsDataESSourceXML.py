import FWCore.ParameterSet.Config as cms

def CTPPSRPAlignmentCorrectionsDataESSourceXML(**kwargs):
  mod = cms.ESSource('CTPPSRPAlignmentCorrectionsDataESSourceXML',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
