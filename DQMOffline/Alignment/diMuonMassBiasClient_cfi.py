import FWCore.ParameterSet.Config as cms

diMuonMassBiasClient = cms.EDProducer('DiMuonMassBiasClient',
  FolderName = cms.string('DiMuonMassBiasMonitor'),
  fitBackground = cms.bool(False),
  debugMode = cms.bool(False),
  fit_par = cms.PSet(
    mean_par = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    width_par = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    ),
    sigma_par = cms.vdouble(
      3.4028234663852886e+38,
      3.4028234663852886e+38,
      3.4028234663852886e+38
    )
  ),
  MEtoHarvest = cms.vstring(
    'DiMuMassVsMuMuPhi',
    'DiMuMassVsMuMuEta',
    'DiMuMassVsMuPlusPhi',
    'DiMuMassVsMuPlusEta',
    'DiMuMassVsMuMinusPhi',
    'DiMuMassVsMuMinusEta',
    'DiMuMassVsMuMuDeltaEta',
    'DiMuMassVsCosThetaCS'
  ),
  mightGet = cms.optional.untracked.vstring
)
