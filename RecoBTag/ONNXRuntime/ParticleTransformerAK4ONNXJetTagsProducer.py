import FWCore.ParameterSet.Config as cms

def ParticleTransformerAK4ONNXJetTagsProducer(*args, **kwargs):
  mod = cms.EDProducer('ParticleTransformerAK4ONNXJetTagsProducer',
    src = cms.InputTag('pfParticleTransformerAK4TagInfos'),
    input_names = cms.vstring(
      'input_1',
      'input_2',
      'input_3',
      'input_4',
      'input_5',
      'input_6'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/RobustParTAK4/PUPPI/V00/modelfile/model.onnx'),
    output_names = cms.vstring('softmax'),
    flav_names = cms.vstring(
      'probb',
      'probbb',
      'problepb',
      'probc',
      'probuds',
      'probg'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
