import FWCore.ParameterSet.Config as cms

def PFDisplacedTrackerVertexProducer(**kwargs):
  mod = cms.EDProducer('PFDisplacedTrackerVertexProducer',
    displacedTrackerVertexColl = cms.InputTag('particleFlowDisplacedVertex'),
    trackColl = cms.InputTag('generalTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
