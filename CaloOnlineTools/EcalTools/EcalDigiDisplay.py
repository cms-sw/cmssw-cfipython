import FWCore.ParameterSet.Config as cms

def EcalDigiDisplay(**kwargs):
  mod = cms.EDAnalyzer('EcalDigiDisplay',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
