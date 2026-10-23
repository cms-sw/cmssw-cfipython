import FWCore.ParameterSet.Config as cms

def HcalDigiColMerger(*args, **kwargs):
  mod = cms.EDProducer('HcalDigiColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
