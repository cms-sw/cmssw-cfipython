import FWCore.ParameterSet.Config as cms

def PATTauDiscriminationByMVAIsolationRun2(**kwargs):
  mod = cms.EDProducer('PATTauDiscriminationByMVAIsolationRun2',
    mvaName = cms.required.string,
    loadMVAfromDB = cms.required.bool,
    inputFileName = cms.optional.FileInPath,
    mvaOpt = cms.required.string,
    srcChargedIsoPtSum = cms.required.string,
    srcNeutralIsoPtSum = cms.required.string,
    srcPUcorrPtSum = cms.required.string,
    srcPhotonPtSumOutsideSignalCone = cms.required.string,
    srcFootprintCorrection = cms.required.string,
    verbosity = cms.int32(0),
    PATTauProducer = cms.InputTag('fixme'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('AND'),
      leadTrack = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      ),
      decayMode = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
