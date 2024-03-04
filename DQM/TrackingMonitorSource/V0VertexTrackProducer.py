import FWCore.ParameterSet.Config as cms

def V0VertexTrackProducer(**kwargs):
  mod = cms.EDProducer('V0VertexTrackProducer',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
