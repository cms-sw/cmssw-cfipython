import FWCore.ParameterSet.Config as cms

def FSQDiJetAve(**kwargs):
  mod = cms.EDProducer('FSQDiJetAve',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
