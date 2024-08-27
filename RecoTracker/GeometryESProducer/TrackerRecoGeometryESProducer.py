import FWCore.ParameterSet.Config as cms

def TrackerRecoGeometryESProducer(**kwargs):
  mod = cms.ESProducer('TrackerRecoGeometryESProducer',
    usePhase2Stacks = cms.bool(False),
    trackerGeometryLabel = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
