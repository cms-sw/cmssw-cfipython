import FWCore.ParameterSet.Config as cms

def HcalPatternSource(**kwargs):
  mod = cms.EDProducer('HcalPatternSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
