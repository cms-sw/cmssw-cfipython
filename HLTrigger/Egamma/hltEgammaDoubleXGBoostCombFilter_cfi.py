import FWCore.ParameterSet.Config as cms

hltEgammaDoubleXGBoostCombFilter = cms.EDFilter('HLTEgammaDoubleXGBoostCombFilter',
  saveTags = cms.bool(True),
  highMassCut = cms.double(95),
  leadCutHighMass1 = cms.vdouble(
    0.98,
    0.95
  ),
  subCutHighMass1 = cms.vdouble(
    0,
    0.04
  ),
  leadCutHighMass2 = cms.vdouble(
    0.85,
    0.85
  ),
  subCutHighMass2 = cms.vdouble(
    0.04,
    0.08
  ),
  leadCutHighMass3 = cms.vdouble(
    0.3,
    0.5
  ),
  subCutHighMass3 = cms.vdouble(
    0.15,
    0.2
  ),
  lowMassCut = cms.double(60),
  leadCutLowMass1 = cms.vdouble(
    0.98,
    0.9
  ),
  subCutLowMass1 = cms.vdouble(
    0.04,
    0.05
  ),
  leadCutLowMass2 = cms.vdouble(
    0.9,
    0.8
  ),
  subCutLowMass2 = cms.vdouble(
    0.1,
    0.1
  ),
  leadCutLowMass3 = cms.vdouble(
    0.6,
    0.6
  ),
  subCutLowMass3 = cms.vdouble(
    0.3,
    0.3
  ),
  candTag = cms.InputTag('hltEgammaCandidatesUnseeded'),
  mvaPhotonTag = cms.InputTag('PhotonXGBoostProducer'),
  mightGet = cms.optional.untracked.vstring
)
