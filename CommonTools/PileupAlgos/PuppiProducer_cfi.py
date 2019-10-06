import FWCore.ParameterSet.Config as cms

PuppiProducer = cms.EDProducer('PuppiProducer',
  puppiDiagnostics = cms.bool(False),
  puppiForLeptons = cms.bool(False),
  UseDeltaZCut = cms.bool(True),
  DeltaZCut = cms.double(0.3),
  PtMaxNeutrals = cms.double(200),
  useExistingWeights = cms.bool(False),
  useWeightsNoLep = cms.bool(False),
  clonePackedCands = cms.bool(False),
  vtxNdofCut = cms.int32(4),
  vtxZCut = cms.double(24),
  candName = cms.InputTag('particleFlow'),
  vertexName = cms.InputTag('offlinePrimaryVertices'),
  applyCHS = cms.bool(True),
  invertPuppi = cms.bool(False),
  useExp = cms.bool(False),
  MinPuppiWeight = cms.double(0.01),
  algos = cms.VPSet(
    cms.PSet(
      EtaMaxExtrap = cms.double(2),
      MedEtaSF = cms.vdouble(1),
      MinNeutralPt = cms.vdouble(0.2),
      MinNeutralPtSlope = cms.vdouble(0.015),
      RMSEtaSF = cms.vdouble(1),
      etaMax = cms.vdouble(2.5),
      etaMin = cms.vdouble(0),
      ptMin = cms.vdouble(0),
      puppiAlgos = cms.VPSet(
        cms.PSet(
          algoId = cms.int32(5),
          applyLowPUCorr = cms.bool(False),
          combOpt = cms.int32(5),
          cone = cms.double(0.4),
          rmsPtMin = cms.double(0.1),
          rmsScaleFactor = cms.double(1),
          useCharged = cms.bool(False)
        )
      )
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
