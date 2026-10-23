import FWCore.ParameterSet.Config as cms

def FSQDiJetAve(*args, **kwargs):
  mod = cms.EDProducer('FSQDiJetAve',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
