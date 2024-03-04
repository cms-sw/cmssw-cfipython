import FWCore.ParameterSet.Config as cms

def MahiDebugger(**kwargs):
  mod = cms.EDAnalyzer('MahiDebugger',
    recoLabel = cms.required.InputTag,
    dynamicPed = cms.required.bool,
    calculateArrivalTime = cms.required.bool,
    timeAlgo = cms.required.int32,
    thEnergeticPulse = cms.required.double,
    ts4Thresh = cms.required.double,
    chiSqSwitch = cms.required.double,
    applyTimeSlew = cms.required.bool,
    meanTime = cms.required.double,
    timeSigmaHPD = cms.required.double,
    timeSigmaSiPM = cms.required.double,
    activeBXs = cms.required.vint32,
    nMaxItersMin = cms.required.int32,
    nMaxItersNNLS = cms.required.int32,
    deltaChiSqThresh = cms.required.double,
    nnlsThresh = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
