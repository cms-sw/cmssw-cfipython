import FWCore.ParameterSet.Config as cms

def DiMuonMassBiasClient(*args, **kwargs):
  mod = cms.EDProducer('DiMuonMassBiasClient',
    FolderName = cms.string('DiMuonMassBiasMonitor'),
    useTH1s = cms.bool(False),
    useBWtimesCB = cms.bool(False),
    fitBackground = cms.bool(False),
    useRooCMSShape = cms.bool(False),
    useRooCBShape = cms.bool(False),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
