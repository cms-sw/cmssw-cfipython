import FWCore.ParameterSet.Config as cms

def HLTVertexPerformanceAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTVertexPerformanceAnalyzer',
    SimVertexCollection = cms.InputTag('g4SimHits'),
    TriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
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
    Vertex = cms.VInputTag('hltVerticesPF'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
