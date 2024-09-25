import FWCore.ParameterSet.Config as cms

def TrackerRecoGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrackerRecoGeometryESProducer',
    usePhase2Stacks = cms.bool(False),
    trackerGeometryLabel = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
