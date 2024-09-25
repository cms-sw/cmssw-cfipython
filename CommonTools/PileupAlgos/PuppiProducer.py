import FWCore.ParameterSet.Config as cms

def PuppiProducer(*args, **kwargs):
  mod = cms.EDProducer('PuppiProducer',
    puppiDiagnostics = cms.bool(False),
    puppiNoLep = cms.bool(False),
    UseFromPVLooseTight = cms.bool(False),
    UseFromPV2Recovery = cms.bool(False),
    UseDeltaZCut = cms.bool(True),
    UseDeltaZCutForPileup = cms.bool(True),
    DeltaZCut = cms.double(0.3),
    EtaMinUseDeltaZ = cms.double(0),
    PtMaxCharged = cms.double(-1),
    EtaMaxCharged = cms.double(99999),
    PtMaxPhotons = cms.double(-1),
    EtaMaxPhotons = cms.double(2.5),
    PtMaxNeutrals = cms.double(200),
    PtMaxNeutralsStartSlope = cms.double(0),
    PtMinForFromPV2Recovery = cms.double(0),
    NumOfPUVtxsForCharged = cms.uint32(0),
    DeltaZCutForChargedFromPUVtxs = cms.double(0.2),
    useExistingWeights = cms.bool(False),
    applyPhotonProtectionForExistingWeights = cms.bool(False),
    clonePackedCands = cms.bool(False),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24),
    candName = cms.InputTag('particleFlow'),
    vertexName = cms.InputTag('offlinePrimaryVertices'),
    useVertexAssociation = cms.bool(False),
    vertexAssociationQuality = cms.int32(0),
    vertexAssociation = cms.InputTag(''),
    applyCHS = cms.bool(True),
    invertPuppi = cms.bool(False),
    useExp = cms.bool(False),
    MinPuppiWeight = cms.double(0.01),
    usePUProxyValue = cms.bool(False),
    PUProxyValue = cms.InputTag(''),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
