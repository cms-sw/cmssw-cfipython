import FWCore.ParameterSet.Config as cms

def CSCL1TPLookupTableEP(**kwargs):
  mod = cms.ESSource('CSCL1TPLookupTableEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
