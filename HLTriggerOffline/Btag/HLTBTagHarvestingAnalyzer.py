import FWCore.ParameterSet.Config as cms

def HLTBTagHarvestingAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTBTagHarvestingAnalyzer',
    mainFolder = cms.string('HLT/BTV/Validation'),
    HLTPathNames = cms.vstring(
      'HLT_PFMET120_PFMHT120_IDTight_v',
      'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_v',
      'HLT_PFHT400_SixPFJet32_PNet2BTagMean0p50_v',
      'HLT_PFHT450_SixPFJet36_PNetBTag0p35_v',
      'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_v',
      'HLT_BTagMu_AK4DiJet20_Mu5_v',
      'HLT_BTagMu_AK4DiJet20_Mu5_v',
      'HLT_BTagMu_AK4DiJet20_Mu5_v'
    ),
    histoName = cms.vstring(
      'hltParticleNetDiscriminatorsJetTags',
      'hltParticleNetDiscriminatorsJetTags',
      'hltParticleNetDiscriminatorsJetTags',
      'hltParticleNetDiscriminatorsJetTags',
      'hltParticleNetDiscriminatorsJetTags',
      'hltBSoftMuonDiJet20L1FastJetL25Jets',
      'hltDeepJetDiscriminatorsJetTags',
      'hltParticleNetDiscriminatorsJetTags'
    ),
    minTag = cms.double(0.2),
    mcFlavours = cms.PSet(
      light = cms.vuint32(
        1,
        2,
        3,
        21
      ),
      c = cms.vuint32(4),
      b = cms.vuint32(5),
      g = cms.vuint32(21),
      uds = cms.vuint32(
        1,
        2,
        3
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
