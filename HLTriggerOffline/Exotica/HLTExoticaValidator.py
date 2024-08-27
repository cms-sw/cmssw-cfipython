import FWCore.ParameterSet.Config as cms

def HLTExoticaValidator(**kwargs):
  mod = cms.EDProducer('HLTExoticaValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
