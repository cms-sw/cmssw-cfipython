import FWCore.ParameterSet.Config as cms

def CandPtrProjector(*args, **kwargs):
  mod = cms.EDProducer('CandPtrProjector',
    src = cms.required.InputTag,
    veto = cms.required.InputTag,
    useDeltaRforFootprint = cms.bool(False),
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
