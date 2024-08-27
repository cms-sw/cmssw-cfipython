import FWCore.ParameterSet.Config as cms

def TrackCollectionFilterCloner(**kwargs):
  mod = cms.EDProducer('TrackCollectionFilterCloner',
    originalSource = cms.InputTag(''),
    originalMVAVals = cms.InputTag(''),
    originalQualVals = cms.InputTag(''),
    minQuality = cms.string('loose'),
    copyExtras = cms.untracked.bool(True),
    copyTrajectories = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
