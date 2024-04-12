import FWCore.ParameterSet.Config as cms

hltEgammaDoubleXGBoostCombFilter = cms.EDFilter('HLTEgammaDoubleXGBoostCombFilter',
  saveTags = cms.bool(True),
  highMassCut = cms.double(90),
  leadCutHighMass1 = cms.vdouble(
    0.92,
    0.95
  ),
  subCutHighMass1 = cms.vdouble(
    0.02,
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
    0.14,
    0.2
  ),
  candTag = cms.InputTag('hltEgammaCandidatesUnseeded'),
  mvaPhotonTag = cms.InputTag('PhotonXGBoostProducer'),
  mightGet = cms.optional.untracked.vstring
)
