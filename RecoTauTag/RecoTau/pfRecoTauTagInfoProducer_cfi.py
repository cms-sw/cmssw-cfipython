import FWCore.ParameterSet.Config as cms

from .PFRecoTauTagInfoProducer import PFRecoTauTagInfoProducer

pfRecoTauTagInfoProducer = PFRecoTauTagInfoProducer(

  ChargedHadrCand_AssociationCone = 0.8,
  PFJetTracksAssociatorProducer = ('ak4PFJetTracksAssociatorAtVertex')
)
