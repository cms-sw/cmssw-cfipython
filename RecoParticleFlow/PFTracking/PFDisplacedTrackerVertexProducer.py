import FWCore.ParameterSet.Config as cms

def PFDisplacedTrackerVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('PFDisplacedTrackerVertexProducer',
    displacedTrackerVertexColl = cms.InputTag('particleFlowDisplacedVertex'),
    trackColl = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
