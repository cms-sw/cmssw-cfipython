import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByIsolationMVA2(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByIsolationMVA2',
    mvaName = cms.required.string,
    loadMVAfromDB = cms.required.bool,
    inputFileName = cms.optional.FileInPath,
    mvaOpt = cms.required.string,
    srcTauTransverseImpactParameters = cms.required.InputTag,
    srcBasicTauDiscriminators = cms.required.InputTag,
    srcChargedIsoPtSumIndex = cms.required.int32,
    srcNeutralIsoPtSumIndex = cms.required.int32,
    srcPUcorrPtSumIndex = cms.required.int32,
    verbosity = cms.int32(0),
    PFTauProducer = cms.InputTag('fixme'),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
