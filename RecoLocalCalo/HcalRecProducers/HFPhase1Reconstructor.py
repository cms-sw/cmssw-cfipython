import FWCore.ParameterSet.Config as cms

def HFPhase1Reconstructor(*args, **kwargs):
  mod = cms.EDProducer('HFPhase1Reconstructor',
    inputLabel = cms.required.InputTag,
    algoConfigClass = cms.required.string,
    setNoiseFlags = cms.required.bool,
    runHFStripFilter = cms.bool(False),
    useChannelQualityFromDB = cms.required.bool,
    checkChannelQualityForDepth3and4 = cms.required.bool,
    algorithm = cms.PSet(
      tlimits = cms.vdouble(
        -10000,
        10000,
        -10000,
        10000
      ),
      energyWeights = cms.required.vdouble,
      soiPhase = cms.uint32(1),
      timeShift = cms.double(0),
      triseIfNoTDC = cms.double(-100),
      tfallIfNoTDC = cms.double(-101),
      minChargeForUndershoot = cms.double(10000000000),
      minChargeForOvershoot = cms.double(10000000000),
      alwaysCalculateQAsymmetry = cms.bool(True),
      Class = cms.string('HFSimpleTimeCheck'),
      rejectAllFailures = cms.bool(False)
    ),
    HFStripFilter = cms.PSet(
      stripThreshold = cms.double(40),
      maxThreshold = cms.double(100),
      timeMax = cms.double(6),
      maxStripTime = cms.double(10),
      wedgeCut = cms.double(0.05),
      seedHitIetaMax = cms.int32(35),
      gap = cms.int32(2),
      lstrips = cms.int32(2),
      verboseLevel = cms.untracked.int32(0)
    ),
    S9S1stat = cms.PSet(),
    S8S1stat = cms.PSet(),
    PETstat = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
