import FWCore.ParameterSet.Config as cms

def PATTauDiscriminationAgainstElectronMVA6(*args, **kwargs):
  mod = cms.EDProducer('PATTauDiscriminationAgainstElectronMVA6',
    method = cms.string('BDTG'),
    loadMVAfromDB = cms.bool(True),
    returnMVA = cms.bool(True),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_woGwGSF_BL = cms.string('gbr_woGwGSF_BL'),
    mvaName_wGwGSF_BL = cms.string('gbr_wGwGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_woGwGSF_EC = cms.string('gbr_woGwGSF_EC'),
    mvaName_wGwGSF_EC = cms.string('gbr_wGwGSF_EC'),
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    isPhase2 = cms.bool(False),
    srcElectrons = cms.InputTag('fixme'),
    vetoEcalCracks = cms.bool(True),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    PATTauProducer = cms.InputTag('fixme'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('AND'),
      leadTrack = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      ),
      decayMode = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
