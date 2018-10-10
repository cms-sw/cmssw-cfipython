import FWCore.ParameterSet.Config as cms

selectedElectronFEDListProducerRecoElectronRecoRecoEcalCandidate = cms.EDProducer('SelectedElectronFEDListProducerGsf',
  electronTags = cms.VInputTag('hltEgammaGsfElectrons'),
  recoEcalCandidateTags = cms.VInputTag('hltL1EG25Ele27WP85GsfTrackIsoFilter'),
  ESLookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
  HBHERecHitTag = cms.InputTag('hltHbhereco'),
  beamSpotTag = cms.InputTag('hltOnlineBeamSpot'),
  rawDataTag = cms.InputTag('rawDataCollector'),
  addThisSelectedFEDs = cms.vint32(
    812,
    813
  ),
  isGsfElectronCollection = cms.vint32(1),
  outputLabelModule = cms.string('StreamElectronRawFed'),
  dumpSelectedSiPixelFed = cms.bool(True),
  dumpSelectedSiStripFed = cms.bool(True),
  dumpSelectedEcalFed = cms.bool(True),
  dumpSelectedHCALFed = cms.bool(True),
  dPhiPixelRegion = cms.double(0.3),
  dEtaPixelRegion = cms.double(0.3),
  dRStripRegion = cms.double(0.3),
  dRHcalRegion = cms.double(0.3),
  maxZPixelRegion = cms.double(24),
  dumpAllTrackerFed = cms.bool(False),
  dumpAllEcalFed = cms.bool(False),
  dumpAllHcalFed = cms.bool(False)
)
