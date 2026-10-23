import FWCore.ParameterSet.Config as cms

def PackedCandidatePrimaryVertexSorter(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidatePrimaryVertexSorter',
    sorting = cms.PSet(),
    assignment = cms.PSet(
      maxDzSigForPrimaryAssignment = cms.double(5),
      maxDzForPrimaryAssignment = cms.double(0.1),
      maxDzErrorForPrimaryAssignment = cms.double(0.05),
      maxDtSigForPrimaryAssignment = cms.double(3),
      maxJetDeltaR = cms.double(0.5),
      minJetPt = cms.double(25),
      maxDistanceToJetAxis = cms.double(0.07),
      maxDzForJetAxisAssigment = cms.double(0.1),
      maxDxyForJetAxisAssigment = cms.double(0.1),
      maxDxySigForNotReconstructedPrimary = cms.double(2),
      maxDxyForNotReconstructedPrimary = cms.double(0.01),
      useTiming = cms.bool(False),
      useVertexFit = cms.bool(True),
      preferHighRanked = cms.bool(False),
      NumOfPUVtxsForCharged = cms.uint32(0),
      DzCutForChargedFromPUVtxs = cms.double(0.2),
      PtMaxCharged = cms.double(-1),
      EtaMinUseDz = cms.double(-1),
      OnlyUseFirstDz = cms.bool(False)
    ),
    qualityForPrimary = cms.int32(3),
    usePVMET = cms.bool(True),
    particles = cms.InputTag('packedPFCandidates'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    jets = cms.InputTag('slimmedJets'),
    produceAssociationToOriginalVertices = cms.bool(True),
    produceSortedVertices = cms.bool(True),
    producePileUpCollection = cms.bool(True),
    produceNoPileUpCollection = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
