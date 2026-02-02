import FWCore.ParameterSet.Config as cms

from .PFRecoTauTagInfoProducer import PFRecoTauTagInfoProducer

pfRecoTauTagInfoProducerInsideOut = PFRecoTauTagInfoProducer(
  tkminTrackerHitsn = 3,
  tkminPt = 0.5,
  tkmaxChi2 = 100,
  ChargedHadrCand_AssociationCone = 1,
  ChargedHadrCand_tkminTrackerHitsn = 3,
  ChargedHadrCand_tkmaxChi2 = 100,
  tkPVmaxDZ = 0.2,
  GammaCand_EcalclusMinEt = 1,
  tkminPixelHitsn = 0,
  PVProducer = ('offlinePrimaryVertices'),
  PFCandidateProducer = ('particleFlow'),
  ChargedHadrCand_tkminPt = 0.5,
  ChargedHadrCand_tkmaxipt = 0.03,
  ChargedHadrCand_tkminPixelHitsn = 0,
  UsePVconstraint = True,
  NeutrHadrCand_HcalclusMinEt = 1,
  PFJetTracksAssociatorProducer = ('insideOutJetTracksAssociatorAtVertex'),
  smearedPVsigmaY = 0.0015,
  smearedPVsigmaX = 0.0015,
  smearedPVsigmaZ = 0.005,
  ChargedHadrCand_tkPVmaxDZ = 0.2,
  tkmaxipt = 0.03
)
