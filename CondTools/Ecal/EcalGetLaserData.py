import FWCore.ParameterSet.Config as cms

def EcalGetLaserData(**kwargs):
  mod = cms.EDAnalyzer('EcalGetLaserData',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
