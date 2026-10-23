import FWCore.ParameterSet.Config as cms

def ME0StubProducer(*args, **kwargs):
  mod = cms.EDProducer('ME0StubProducer',
    InputCollection = cms.InputTag('gemPadDigis'),
    skipCentroids = cms.bool(False),
    layerThresholdPatternId = cms.vint32(
      7,
      7,
      7,
      7,
      7,
      7,
      7,
      7,
      7,
      7,
      5,
      5,
      4,
      4,
      4,
      4,
      4
    ),
    layerThresholdEta = cms.vint32(
      4,
      5,
      4,
      5,
      4,
      5,
      4,
      5,
      4,
      5,
      4,
      5,
      4,
      5,
      4
    ),
    maxSpan = cms.int32(37),
    width = cms.int32(192),
    deghostPre = cms.bool(True),
    deghostPost = cms.bool(True),
    groupWidth = cms.int32(8),
    ghostWidth = cms.int32(1),
    xPartitionEnabled = cms.bool(True),
    enableNonPointing = cms.bool(False),
    crossPartitionSegmentWidth = cms.int32(4),
    numOutputs = cms.int32(4),
    checkIds = cms.bool(False),
    edgeDistance = cms.int32(2),
    numOr = cms.int32(2),
    mseThreshold = cms.double(0.75),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
