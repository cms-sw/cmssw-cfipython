import FWCore.ParameterSet.Config as cms

def EcalChannelStatusAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalChannelStatusAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
