import FWCore.ParameterSet.Config as cms

def HLTParticleTransformerAK4ONNXJetTagsProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTParticleTransformerAK4ONNXJetTagsProducer',
    src = cms.InputTag('hltParticleTransformerAK4TagInfos'),
    input_names = cms.vstring(
      'global_features',
      'cpf_features',
      'vtx_features'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/HLT/hltParticleTransformerAK4/hltParTAK4_CMSSW15_082026.onnx'),
    output_names = cms.vstring('output'),
    flav_names = cms.vstring(
      'probb',
      'probbb',
      'problepb'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
