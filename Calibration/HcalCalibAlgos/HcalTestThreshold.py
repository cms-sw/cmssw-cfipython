import FWCore.ParameterSet.Config as cms

def HcalTestThreshold(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTestThreshold',
    etaMin = cms.int32(-85),
    etaMax = cms.int32(85),
    phiValue = cms.int32(1),
    ixEENumbers = cms.vint32(
      1,
      10,
      20,
      30,
      39
    ),
    iyEENumbers = cms.vint32(
      41,
      43,
      45,
      47
    ),
    EBHitEnergyThreshold = cms.double(0.08),
    EEHitEnergyThreshold0 = cms.double(0.3),
    EEHitEnergyThreshold1 = cms.double(0),
    EEHitEnergyThreshold2 = cms.double(0),
    EEHitEnergyThreshold3 = cms.double(0),
    EEHitEnergyThresholdLow = cms.double(0.3),
    EEHitEnergyThresholdHigh = cms.double(0.3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
