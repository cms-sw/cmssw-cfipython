import FWCore.ParameterSet.Config as cms

def V0VertexTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('V0VertexTrackProducer',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
