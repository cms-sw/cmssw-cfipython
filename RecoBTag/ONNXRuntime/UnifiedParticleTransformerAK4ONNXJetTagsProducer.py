import FWCore.ParameterSet.Config as cms

def UnifiedParticleTransformerAK4ONNXJetTagsProducer(**kwargs):
  mod = cms.EDProducer('UnifiedParticleTransformerAK4ONNXJetTagsProducer',
    src = cms.InputTag('pfUnifiedParticleTransformerAK4TagInfos'),
    input_names = cms.vstring(
      'input_1',
      'input_2',
      'input_3',
      'input_4',
      'input_5',
      'input_6',
      'input_7',
      'input_8'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/UParTAK4/PUPPI/V00/UParTAK4.onnx'),
    output_names = cms.vstring('softmax'),
    flav_names = cms.vstring(
      'probb',
      'probbb',
      'problepb',
      'probc',
      'probs',
      'probu',
      'probd',
      'probg',
      'probele',
      'probmu',
      'probtaup1h0p',
      'probtaup1h1p',
      'probtaup1h2p',
      'probtaup3h0p',
      'probtaup3h1p',
      'probtaum1h0p',
      'probtaum1h1p',
      'probtaum1h2p',
      'probtaum3h0p',
      'probtaum3h1p',
      'ptcorr',
      'ptreshigh',
      'ptreslow',
      'ptnu',
      'probemudata',
      'probemumc',
      'probdimudata',
      'probdimumc',
      'probmutaudata',
      'probmutaumc'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
