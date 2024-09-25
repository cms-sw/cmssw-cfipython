import FWCore.ParameterSet.Config as cms

def HGCalPartialWaferTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalPartialWaferTester',
    nameSense = cms.string('HGCalHESiliconSensitive'),
    waferOrientations = cms.vint32(
      0,
      1,
      2,
      3,
      4,
      5
    ),
    partialTypes = cms.vint32(
      11,
      12,
      13,
      14,
      15,
      16,
      21,
      22,
      23,
      24,
      25
    ),
    numberOfTrials = cms.int32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
