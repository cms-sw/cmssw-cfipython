import FWCore.ParameterSet.Config as cms

def EcalSimRawData(**kwargs):
  mod = cms.EDAnalyzer('EcalSimRawData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
