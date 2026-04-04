import FWCore.ParameterSet.Config as cms

def IPTCorrector(*args, **kwargs):
  mod = cms.EDProducer('IPTCorrector',
    corTracksLabel = cms.InputTag('hltIter0PFlowCtfWithMaterialTracks'),
    filterLabel = cms.InputTag('hltIsolPixelTrackL2Filter'),
    associationCone = cms.double(0.2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
