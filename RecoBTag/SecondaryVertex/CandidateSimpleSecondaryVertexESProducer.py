import FWCore.ParameterSet.Config as cms

def CandidateSimpleSecondaryVertexESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateSimpleSecondaryVertexESProducer',
    use3d = cms.bool(True),
    useSignificance = cms.bool(True),
    unBoost = cms.bool(False),
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(1),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
