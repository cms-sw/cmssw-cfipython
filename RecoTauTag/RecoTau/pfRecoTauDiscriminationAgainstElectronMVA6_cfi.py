import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstElectronMVA6 = cms.EDProducer('PFRecoTauDiscriminationAgainstElectronMVA6',
  minMVANoEleMatchWOgWOgsfBL = cms.double(0),
  PFTauProducer = cms.InputTag('pfTauProducer'),
  minMVANoEleMatchWgWOgsfBL = cms.double(0),
  mvaName_wGwGSF_EC = cms.string('gbr_wGwGSF_EC'),
  minMVAWgWgsfBL = cms.double(0),
  mvaName_woGwGSF_EC = cms.string('gbr_woGwGSF_EC'),
  minMVAWOgWgsfEC = cms.double(0),
  mvaName_wGwGSF_BL = cms.string('gbr_wGwGSF_BL'),
  mvaName_woGwGSF_BL = cms.string('gbr_woGwGSF_BL'),
  returnMVA = cms.bool(True),
  loadMVAfromDB = cms.bool(True),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  ),
  mvaName_NoEleMatch_woGwoGSF_BL = cms.string('gbr_NoEleMatch_woGwoGSF_BL'),
  vetoEcalCracks = cms.bool(True),
  usePhiAtEcalEntranceExtrapolation = cms.bool(False),
  mvaName_NoEleMatch_wGwoGSF_BL = cms.string('gbr_NoEleMatch_wGwoGSF_BL'),
  minMVANoEleMatchWOgWOgsfEC = cms.double(0),
  minMVAWOgWgsfBL = cms.double(0),
  minMVAWgWgsfEC = cms.double(0),
  verbosity = cms.int32(0),
  mvaName_NoEleMatch_wGwoGSF_EC = cms.string('gbr_NoEleMatch_wGwoGSF_EC'),
  method = cms.string('BDTG'),
  srcGsfElectrons = cms.InputTag('gedGsfElectrons'),
  mvaName_NoEleMatch_woGwoGSF_EC = cms.string('gbr_NoEleMatch_woGwoGSF_EC'),
  minMVANoEleMatchWgWOgsfEC = cms.double(0)
)
