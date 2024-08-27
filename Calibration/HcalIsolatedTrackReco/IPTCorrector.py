import FWCore.ParameterSet.Config as cms

def IPTCorrector(**kwargs):
  mod = cms.EDProducer('IPTCorrector',
    corTracksLabel = cms.InputTag('hltIter0PFlowCtfWithMaterialTracks'),
    filterLabel = cms.InputTag('hltIsolPixelTrackL2Filter'),
    associationCone = cms.double(0.2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
