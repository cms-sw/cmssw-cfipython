import FWCore.ParameterSet.Config as cms

def EcalTPGParamReaderFromDB(**kwargs):
  mod = cms.EDAnalyzer('EcalTPGParamReaderFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
