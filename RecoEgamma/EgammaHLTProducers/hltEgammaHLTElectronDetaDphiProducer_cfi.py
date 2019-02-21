import FWCore.ParameterSet.Config as cms

hltEgammaHLTElectronDetaDphiProducer = cms.EDProducer('EgammaHLTElectronDetaDphiProducer',
  electronProducer = cms.InputTag('hltEleAnyWP80PixelMatchElectronsL1Seeded'),
  BSProducer = cms.InputTag('hltOnlineBeamSpot'),
  recoEcalCandidateProducer = cms.InputTag(''),
  useSCRefs = cms.bool(False),
  useTrackProjectionToEcal = cms.bool(False),
  variablesAtVtx = cms.bool(True)
)
