import FWCore.ParameterSet.Config as cms

def L1GTProducer(**kwargs):
  mod = cms.EDProducer('L1GTProducer',
    scales = cms.PSet(
      pT_lsb = cms.required.double,
      phi_lsb = cms.required.double,
      eta_lsb = cms.required.double,
      z0_lsb = cms.required.double,
      isolationPT_lsb = cms.required.double,
      beta_lsb = cms.required.double,
      mass_lsb = cms.required.double,
      seed_pT_lsb = cms.required.double,
      seed_z0_lsb = cms.required.double,
      scalarSumPT_lsb = cms.required.double,
      sum_pT_pv_lsb = cms.required.double,
      pos_chg = cms.required.int32,
      neg_chg = cms.required.int32
    ),
    GTTPromptJets = cms.required.InputTag,
    GTTDisplacedJets = cms.required.InputTag,
    GTTPromptHtSum = cms.required.InputTag,
    GTTDisplacedHtSum = cms.required.InputTag,
    GTTEtSum = cms.required.InputTag,
    GTTPrimaryVert = cms.required.InputTag,
    GMTSaPromptMuons = cms.required.InputTag,
    GMTSaDisplacedMuons = cms.required.InputTag,
    GMTTkMuons = cms.required.InputTag,
    CL2JetsSC4 = cms.required.InputTag,
    CL2JetsSC8 = cms.required.InputTag,
    CL2Photons = cms.required.InputTag,
    CL2Electrons = cms.required.InputTag,
    CL2Taus = cms.required.InputTag,
    CL2EtSum = cms.required.InputTag,
    CL2HtSum = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
