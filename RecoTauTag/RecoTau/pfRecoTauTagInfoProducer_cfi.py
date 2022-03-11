import FWCore.ParameterSet.Config as cms

pfRecoTauTagInfoProducer = cms.EDProducer('PFRecoTauTagInfoProducer',
  tkminTrackerHitsn = cms.int32(3),
  tkminPt = cms.double(0.5),
  tkmaxChi2 = cms.double(100),
  ChargedHadrCand_AssociationCone = cms.double(0.8),
  ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
  ChargedHadrCand_tkmaxChi2 = cms.double(100),
  tkPVmaxDZ = cms.double(0.2),
  GammaCand_EcalclusMinEt = cms.double(1),
  tkminPixelHitsn = cms.int32(0),
  PVProducer = cms.InputTag('offlinePrimaryVertices'),
  PFCandidateProducer = cms.InputTag('particleFlow'),
  ChargedHadrCand_tkminPt = cms.double(0.5),
  ChargedHadrCand_tkmaxipt = cms.double(0.03),
  ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
  UsePVconstraint = cms.bool(True),
  NeutrHadrCand_HcalclusMinEt = cms.double(1),
  PFJetTracksAssociatorProducer = cms.InputTag('ak4PFJetTracksAssociatorAtVertex'),
  smearedPVsigmaY = cms.double(0.0015),
  smearedPVsigmaX = cms.double(0.0015),
  smearedPVsigmaZ = cms.double(0.005),
  ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
  tkmaxipt = cms.double(0.03),
  mightGet = cms.optional.untracked.vstring
)
