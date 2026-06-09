import FWCore.ParameterSet.Config as cms

def TrackCollectionFilterCloner(*args, **kwargs):
  mod = cms.EDProducer('TrackCollectionFilterCloner',
    originalSource = cms.InputTag(''),
    originalMVAVals = cms.InputTag(''),
    originalQualVals = cms.InputTag(''),
    minQuality = cms.string('loose'),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
