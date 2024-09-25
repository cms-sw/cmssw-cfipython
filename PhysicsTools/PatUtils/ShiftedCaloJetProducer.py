import FWCore.ParameterSet.Config as cms

def ShiftedCaloJetProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedCaloJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
