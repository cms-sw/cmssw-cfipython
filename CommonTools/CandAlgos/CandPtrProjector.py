import FWCore.ParameterSet.Config as cms

def CandPtrProjector(**kwargs):
  mod = cms.EDProducer('CandPtrProjector',
    src = cms.required.InputTag,
    veto = cms.required.InputTag,
    useDeltaRforFootprint = cms.bool(False),
    extendVetoBySingleSourcePtr = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
